# Browser Requirements

This sample page demonstrates how to format content in DocFX markdown.

## Supported Browsers

The XMPro platform can be run on a variety of browsers and operating systems. The latest two major releases of the following browsers are supported on the indicated operating systems:

| Browser | Windows | macOS | iOS | Android |
|---------|---------|-------|-----|---------|
| Google Chrome | ✓ | ✓ | ✓ | ✓ |
| Apple Safari | ✗ | ✓ | ✓ | ✗ |
| Microsoft Edge | ✓ | ✓ | ✗ | ✗ |
| Mozilla Firefox | ✓ | ✓ | ✗ | ✗ |
| Opera | ✓ | ✓ | ✗ | ✗ |

## Alerts

DocFX supports various types of alerts:

> [!NOTE]
> This is a note alert. Use it for general information.

> [!TIP]
> This is a tip alert. Use it for helpful tips.

> [!WARNING]
> This is a warning alert. Use it for important warnings.

> [!CAUTION]
> This is a caution alert. Use it for critical information.

> [!IMPORTANT]
> This is an important alert. Use it for essential information.

## Code Blocks

DocFX supports code blocks with syntax highlighting:

```csharp
public class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Hello, World!");
    }
}
```

```javascript
function sayHello() {
    console.log("Hello, World!");
}
```

```json
{
    "name": "John Doe",
    "age": 30,
    "isActive": true
}
```

## Tabs

DocFX supports tabs:

# [Windows](#tab/windows)

This content is for Windows users.

# [macOS](#tab/macos)

This content is for macOS users.

# [Linux](#tab/linux)

This content is for Linux users.

***

## Images

DocFX supports images:

![XMPro Logo](../images/xmpro-logo.png)

## Links

DocFX supports various types of links:

- [Internal link to Introduction](../introduction.md)
- [Internal link to a section](../concepts/data-stream/index.md)
- [External link to XMPro website](https://xmpro.com/)
- [Link to a section on the same page](#supported-browsers)

## Lists

DocFX supports ordered and unordered lists:

Unordered list:
- Item 1
- Item 2
- Item 3
  - Nested item 1
  - Nested item 2

Ordered list:
1. First item
2. Second item
3. Third item
   1. Nested item 1
   2. Nested item 2

## Tables

DocFX supports tables:

| Name | Description | Required |
|------|-------------|----------|
| id | The unique identifier | Yes |
| name | The display name | Yes |
| description | The description | No |
| type | The data type | Yes |

## Blockquotes

DocFX supports blockquotes:

> This is a blockquote.
> 
> It can span multiple lines.

## Horizontal Rules

DocFX supports horizontal rules:

---

## Emphasis

DocFX supports emphasis:

*Italic text*

**Bold text**

***Bold and italic text***

## Conclusion

This sample page demonstrates the various formatting options available in DocFX markdown. Use this as a reference when migrating content from GitBook to DocFX.
