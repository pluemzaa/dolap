<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4"/>
        <attribute name="authors" value=""/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 10:50:05 PM"/>
        <attribute name="created" value="Z3V5eGE7REVTS1RPUC1TT0JKOEQ5OzI1NjgtMDctMTc7MTA6MDM6NTYgUE07MjkxOQ=="/>
        <attribute name="edited" value="Z3V5eGE7REVTS1RPUC1TT0JKOEQ5OzI1NjgtMDctMTc7MTA6NTA6MDUgUE07NDszMDI2"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="startNum, endNum, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="startNum"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="endNum"/>
            <assign variable="i" expression="startNum"/>
            <while expression="i &lt;= endNum">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>