<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_3"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-20 12:39:21 PM"/>
        <attribute name="created" value="VXNlcjsyNjc4Ny0zMjAxOzI1NjgtMDctMTk7MTA6MTI6NDMgUE07MjIyMQ=="/>
        <attribute name="edited" value="VXNlcjsyNjc4Ny0zMjAxOzI1NjgtMDctMTk7MTA6NDM6NTIgUE07MTsyMzMz"/>
        <attribute name="edited" value="bmFyYXQ7TEVOT1ZPTkFSQVRISVA7MjU2OC0wNy0yMDsxMjozOToyMSBQTTs0OzMwMDM="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="i, j" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;input end number: &quot;" newline="True"/>
            <input variable="j"/>
            <while expression="i&lt;(j+1)">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>